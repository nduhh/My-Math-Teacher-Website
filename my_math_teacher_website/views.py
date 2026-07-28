from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm, WaitingListForm
from .models import Contact, WaitingList
from django.db import IntegrityError

def home(request):
    return render(request, "home.html")

def screenshots(request):
    return render(request, "screenshots.html")

def features(request):
    return render(request, "features.html")

def how_it_works(request):
    return render(request, "how_it_works.html")

def roadmap(request):
    return render(request, "roadmap.html")

# Contact Form View
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message_body = form.cleaned_data['message']

            # Save to database
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_body,
            )

            # Prepare and send email
            full_message = f"""
You have a new message from My Math Teacher website.

From: {name} <{email}>
Subject: {subject}

Message:
{message_body}
            """

            try:
                send_mail(
                    subject=f'Contact Form: {subject}',
                    message=full_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['nntembe1212@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                # Still saved to DB, but notify user of email failure
                messages.warning(
                    request,
                    'Message saved, but email notification failed. We will still get back to you.'
                )

            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def join_waiting_list(request):
    if request.method == 'POST':
        form = WaitingListForm(request.POST)
        if form.is_valid():
            # Save to database - but catch duplicate email error
            try:
                WaitingList.objects.create(
                    full_name=form.cleaned_data['full_name'],
                    email=form.cleaned_data['email'],
                    school=form.cleaned_data.get('school', ''),
                    grade=form.cleaned_data.get('grade', ''),
                    province=form.cleaned_data.get('province', ''),
                )
                messages.success(request, 'You have been added to the waiting list!')
                return redirect('join_waiting_list')
            except IntegrityError:
                # Duplicate email - add a field-specific error
                messages.error(request, 'This email address is already on the waiting list.')
                # form.add_error('email', 'This email is already registered.')
        else:
            # Form validation failed
            messages.error(request, 'Please correct the errors below.')
    else:
        form = WaitingListForm()

    return render(request, 'join_waiting_list.html', {'form': form})