Title: PDF Merger using Python and Django

```python
# models.py

from django.db import models

# Model to handle PDF files
class PDFFile(models.Model):
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"PDF File {self.id}"

```

```python
# forms.py

from django import forms
from .models import PDFFile

# Form for uploading PDF files
class PDFFileForm(forms.ModelForm):
    class Meta:
        model = PDFFile
        fields = ['file']

```

```python
# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PDFFileForm
from .models import PDFFile
from PyPDF2 import PdfMerger

# View to upload PDF files
def upload_pdf(request):
    if request.method == 'POST':
        form = PDFFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('merge_pdfs')
    else:
        form = PDFFileForm()
    return render(request, 'upload_pdf.html', {'form': form})

# View to merge uploaded PDF files
def merge_pdfs(request):
    pdf_files = PDFFile.objects.all()
    if request.method == 'POST' and pdf_files:
        merger = PdfMerger()
        for pdf in pdf_files:
            # Append each PDF file
            merger.append(pdf.file.path)

        # Save the merged PDF to a new file
        merged_file_path = 'media/merged.pdf'
        merger.write(merged_file_path)
        merger.close()

        # Return the merged PDF as a download
        response = HttpResponse(open(merged_file_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="merged.pdf"'
        return response

    return render(request, 'merge_pdfs.html', {'pdf_files': pdf_files})

```

```html
<!-- upload_pdf.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Upload PDF Files</title>
</head>
<body>
    <h1>Upload PDF Files</h1>
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Upload</button>
    </form>
</body>
</html>

```

```html
<!-- merge_pdfs.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Merge PDF Files</title>
</head>
<body>
    <h1>Merge PDF Files</h1>
    <ul>
        {% for pdf in pdf_files %}
            <li>{{ pdf.file.name }}</li>
        {% endfor %}
    </ul>
    {% if pdf_files %}
        <form method="post">
            {% csrf_token %}
            <button type="submit">Merge PDFs</button>
        </form>
    {% else %}
        <p>No PDF files to merge.</p>
    {% endif %}
</body>
</html>

```

```python
# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('merge/', views.merge_pdfs, name='merge_pdfs'),
]

```

```python
# settings.py (add the following settings)

# Static files (CSS, JavaScript, Images)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Installed apps
INSTALLED_APPS = [
    ...
    'your_app_name',  # Add your app name here
]

```

```plaintext
# requirements.txt

Django==3.2.9
PyPDF2==2.11.1

```

# Note: Ensure you have Django and PyPDF2 installed, and replace `your_app_name` with your app's name in the `INSTALLED_APPS` list in settings.py.
```