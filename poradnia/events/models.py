from datetime import timedelta

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from poradnia.events.utils import render_event_icon
from poradnia.records.models import AbstractRecord, AbstractRecordQuerySet
from poradnia.users.models import Profile


class Reminder(TimeStampedModel):
    event = models.ForeignKey(to="Event", on_delete=models.CASCADE)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, help_text=_("Recipient"), on_delete=models.CASCADE
    )
    active = models.BooleanField(default=True, help_text=_("Active status"))

    class Meta:
        verbose_name = _("Reminder")
        verbose_name_plural = _("Reminders")


class EventQuerySet(AbstractRecordQuerySet):
    def old(self):
        return self.filter(time__lte=now())

    def fresh(self):
        max_days = max(day for day, _ in Profile.EVENT_REMINDER_CHOICE)
        return self.filter(time__gte=now() - timedelta(days=max_days))


class Event(AbstractRecord):
    deadline = models.BooleanField(
        default=True,
        verbose_name=_("Dead-line"),
        help_text=_(
            "A significant event, especially highlighted, "
            "for example, in the list of cases."
        ),
    )
    completed = models.BooleanField(
        default=False,
        verbose_name=_("Completed"),
        help_text=_("Event has been completed, no more reminders."),
    )
    public = models.BooleanField(
        default=False,
        verbose_name=_("Public"),
        help_text=_("Event is visible to customers (ext)."),
    )
    time = models.DateTimeField(verbose_name=_("Time"))
    text = models.TextField(verbose_name=_("Subject"))
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="event_created_by",
        verbose_name=_("Created by"),
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=_("Created on"))
    modified_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name=_("Modified by"),
        null=True,
        on_delete=models.CASCADE,
        related_name="event_modified_by",
    )
    modified_on = models.DateTimeField(
        auto_now=True, null=True, blank=True, verbose_name=_("Modified on")
    )
    objects = EventQuerySet.as_manager()

    @property
    def subject(self):
        if len(self.text) > 100:
            return "{} ...".format(self.text[:100])
        return self.text

    def get_absolute_url(self):
        case_url = self.record.case_get_absolute_url()
        return "{}#event-{}".format(case_url, self.pk)

    def get_edit_url(self):
        return reverse("events:edit", kwargs={"pk": self.pk})

    def get_calendar_url(self):
        return reverse(
            "events:calendar", kwargs={"month": self.time.month, "year": self.time.year}
        )

    @property
    def render_deadline(self):
        if self.deadline:
            return render_event_icon(
                "fa-hourglass", "black", "Wydarzenie jest terminem"
            )
        return render_event_icon("fa-hourglass", "gray", "Wydarzenie nie jest terminem")

    @property
    def render_completed(self):
        if self.completed:
            return render_event_icon(
                "fa-check", "black", "Ukończono (nie ma więcej przypomnień)"
            )
        return render_event_icon("fa-check", "gray", "Nie ukończono (są przypomnienia)")

    @property
    def render_public(self):
        if self.public:
            return render_event_icon("fa-globe", "black", "Wydarzenie jest publiczne")
        return render_event_icon("fa-globe", "gray", "Wydarzenie nie jest publiczne")

    @property
    def render_court_session(self):
        if hasattr(self, "courtsession") and self.courtsession:
            return render_event_icon(
                "fa-balance-scale",  # "fa-gavel",
                "black; font-weight: bold; font-size: 17px;",
                "Wydarzenie jest rozprawą sądową",
            )
        return ""

    @property
    def render_calendar_item(self):
        title = self.text
        text = (
            self.render_court_session
            + self.render_deadline
            + self.render_completed
            + self.render_public
            + "<br> "
            + str(self.case)
        )
        url = self.get_absolute_url()
        return mark_safe(
            f'<li class_attr=""><a href="{url}" title="{title}">{text}</a></li>'
        )

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
