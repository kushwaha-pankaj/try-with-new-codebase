Title: Simple PDF Merger Using Django

```python
# Import the required modules
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from PyPDF2 import PdfMerger

# Create a form for uploading PDF files
class PDFUploadForm(forms.Form):
    pdf_files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), 
                                label='Select PDF files to merge')

# The view to handle PDF merge
def merge_pdfs(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Prepare a merger instance
            merger = PdfMerger()

            # Retrieve and iterate over uploaded PDF files
            uploaded_files = request.FILES.getlist('pdf_files')
            for pdf in uploaded_files:
                # Append each PDF to the merger
                merger.append(pdf)

            # Create an HTTP response with the merged PDF
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="merged_document.pdf"'
            
            # Write final merged PDF to the response
            merger.write(response)
            merger.close()

            return response
    else:
        form = PDFUploadForm()

    # Render the upload form
    return render(request, 'merge_pdfs.html', {'form': form})

# merge_pdfs.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PDF Merger</title>
</head>
<body>
    <h1>Upload PDF Files to Merge</h1>
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Merge PDFs</button>
    </form>
</body>
</html>
"""

# urls.py (add the following in your project's urls.py file)
from django.urls import path
from . import views

urlpatterns = [
    path('merge/', views.merge_pdfs, name='merge_pdfs')
]
```

This Django application sets up a simple interface for merging PDF files. Users can upload multiple PDF files using a form, and upon submission, the files are merged and returned as a single PDF document.