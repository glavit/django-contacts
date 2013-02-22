# -*- coding: utf-8 -*
from django.contrib import admin
from contacts.models import Subject
from contacts.models import Message
from contacts.models import CallBack


class SubjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'email', 'created_at', 'updated_at']
	search_fields = ['title', 'email', 'created_at', 'updated_at']
	list_filter = ['email']
	ordering = ['title']

admin.site.register(Subject, SubjectAdmin)


class MessageAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'phone', 'email', 'url', 'status', 'msg', 'ip', 'updated_at')
	search_fields = ('id', 'name', 'phone', 'email', 'url', 'status', 'msg', 'ip', 'updated_at')
	list_filter = ['updated_at', 'status']
	ordering = ['-updated_at']

admin.site.register(Message, MessageAdmin)


class CallBackAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'subject', 'phone', 'from_time', 'to_time', 'ip', 'status']
	search_fields = ['first_name', 'last_name', 'subject', 'phone', 'from_time', 'to_time', 'ip', 'status']
	list_filter = ['subject', 'phone', 'from_time', 'to_time', 'ip', 'status']
	# list_editable = ['status']
	ordering = ['-updated_at']

admin.site.register(CallBack, CallBackAdmin)
