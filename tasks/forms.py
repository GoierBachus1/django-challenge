from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "priority", "is_completed"]

    def clean_title(self):
        title = (self.cleaned_data.get("title") or "").strip()
        if not title:
            raise forms.ValidationError("Title is required.")
        if len(title) > 100:
            raise forms.ValidationError("Title must be at most 100 characters.")
        return title

    def clean_priority(self):
        priority = self.cleaned_data.get("priority")
        valid = {c[0] for c in Task.PRIORITY_CHOICES}
        if priority not in valid:
            raise forms.ValidationError("Priority must be one of : low, medium, high.")
        return priority