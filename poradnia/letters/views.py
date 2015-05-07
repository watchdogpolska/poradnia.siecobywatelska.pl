from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from cases.models import Case
from django.contrib import messages
from django.utils.translation import ugettext as _
from .helpers import formset_attachment_factory
# from crispy_forms.helper import FormHelper
from .forms import NewCaseForm, AddLetterForm, LetterForm, SendLetterForm
from .models import Letter


@login_required
def new_case(request):
    context = {}

    LetterForm = NewCaseForm.partial(user=request.user)
    AttachmentFormSet = formset_attachment_factory()

    formset = None
    if request.method == 'POST':
        form = LetterForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            formset = AttachmentFormSet(request.POST, request.FILES, instance=obj)
            if formset.is_valid():
                obj.save()
                messages.success(request,
                    _("Case about %(object)s created!") % {'object': obj, })
                if obj.created_by != obj.client:
                    obj.client.notify(actor=request.user, verb='created', target=obj, from_email=obj.case.get_email())
                formset.save()
                return HttpResponseRedirect(obj.case.get_absolute_url())
    else:
        form = LetterForm()
    context['form'] = form
    context['formset'] = formset or AttachmentFormSet(instance=Letter())
    return render(request, 'letters/form.html', context)


@login_required
def add(request, case_pk):
    context = {}
    case = get_object_or_404(Case, pk=case_pk)
    case.perm_check(request.user, 'can_add_record')

    LetterForm = AddLetterForm.partial(case=case, user=request.user)
    AttachmentFormSet = formset_attachment_factory()

    formset = None
    if request.method == 'POST':
        form = LetterForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            formset = AttachmentFormSet(request.POST, request.FILES, instance=obj)
            if formset.is_valid():
                obj.save()
                messages.success(request,
                    _("Letter %(object)s created!") % {'object': obj, })
                formset.save()
                return HttpResponseRedirect(case.get_absolute_url())
    else:
        form = LetterForm()
    context['form'] = form
    context['formset'] = formset or AttachmentFormSet(instance=Letter())

    return render(request, 'letters/form.html', context)


@login_required
def send(request, pk):
    context = {}

    letter = get_object_or_404(Letter, pk=pk)
    case = letter.case

    case.perm_check(request.user, 'can_add_record')
    context['letter'] = letter
    context['case'] = case

    if letter.status == Letter.STATUS.done:
        messages.warning(request, _("It doesn't make sense."))
        return HttpResponseRedirect(case.get_absolute_url())

    LetterForm = SendLetterForm.partial(user=request.user, instance=letter)

    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            obj = form.save()
            messages.success(request,
                _("Letter %(object)s send!") % {'object': obj, })
            obj.send_notification(actor=request.user, verb='accepted')
            return HttpResponseRedirect(case.get_absolute_url())
    else:
        form = SendLetterForm(user=request.user, instance=letter)
    context['form'] = form
    return render(request, 'letters/form.html', context)


@login_required
def edit(request, pk):
    context = {}
    letter = get_object_or_404(Letter, pk=pk)
    context['letter'] = letter

    case = letter.case
    context['case'] = case

    if letter.created_by == request.user:
        case.perm_check(request.user, 'can_change_own_record')
    else:
        case.perm_check(request.user, 'can_change_all_record')

    AttachmentFormSet = formset_attachment_factory()
    formset = None
    if request.method == 'POST':
        form = LetterForm(request.POST, user=request.user, instance=letter)
        if form.is_valid():
            obj = form.save(commit=False)
            formset = AttachmentFormSet(request.POST, request.FILES, instance=obj)
            if formset.is_valid():
                obj.save()
                formset.save()
                messages.success(request,
                    _("Letter %(object)s updated!") % {'object': obj, })
                obj.send_notification(actor=request.user, verb='updated')
                return HttpResponseRedirect(obj.case.get_absolute_url())
    else:
        form = LetterForm(user=request.user, instance=letter)
    context['form'] = form
    context['formset'] = formset or AttachmentFormSet(instance=letter)

    return render(request, 'letters/form.html', context)


def detail(request, pk):
    pass
