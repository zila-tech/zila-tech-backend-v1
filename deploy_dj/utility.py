import os


def delete_old_files(sender, instance, field_names, pre_save=False, post_delete=False):
    """
    Delete old files when new files are uploaded or when the object is deleted.

    Args:
        sender: The sender model class.
        instance: The instance of the model.
        field_names: A list of field names (strings) of the file fields.e
        pre_save: Indicates to update.
        post_delete: Indicate you want delete an object
    """
    try:
        # Get the old instance if it's an update
        old_instance = None
        if pre_save:
            old_instance = sender.objects.get(id=instance.id)

            for field_name in field_names:
                # Get the old and new file paths for each field
                old_file_path = (
                    getattr(old_instance, field_name).path
                    if pre_save and old_instance
                    else None
                )
                new_file_path = getattr(instance, field_name).path

                # Delete the old file if it exists and it's different from the new one
                if (
                    old_file_path
                    and old_file_path != new_file_path
                    and os.path.exists(old_file_path)
                ):
                    os.remove(old_file_path)

        elif post_delete:
            """Delete specified file fields for a Django model instance"""
            for field_name in field_names:
                field = getattr(instance, field_name)
                try:
                    field.delete(save=False)
                except Exception as e:
                    pass

    except Exception as e:
        pass
