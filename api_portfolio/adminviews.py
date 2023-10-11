from django.shortcuts import render
from django.http import HttpResponse

from .models import Note


def print_all_selected_objects(request, object_ids):
    # Split the object IDs and retrieve the corresponding objects.
    ids = object_ids.split(",")
    notes = Note.objects.filter(id__in=ids)

    # Create a printable HTML representation of all selected objects.
    printable_content = "<html><head><title>Print All Selected</title></head><body>"
    for note in notes:
        printable_content += "<h2>{}</h2>".format(note.welcome)
        printable_content += "<p>{}</p>".format(note.detail)
    printable_content += "</body></html>"

    # Create a response with the printable HTML content.
    response = HttpResponse(printable_content, content_type="text/html")
    return response


def print_single_object(request, object_id):
    # Retrieve the single object to print.
    note = Note.objects.get(id=object_id)

    # Create a printable HTML representation of the single object.
    printable_content = "<html><head><title>Print Note</title></head><body>"
    printable_content += "<h2>{}</h2>".format(note.welcome)
    printable_content += "<p>{}</p>".format(note.detail)
    printable_content += "</body></html>"

    # Create a response with the printable HTML content.
    response = HttpResponse(printable_content, content_type="text/html")
    return response
