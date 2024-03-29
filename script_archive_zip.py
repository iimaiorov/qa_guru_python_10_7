import os
import zipfile
import glob


def archive_data_to_zip(data_path, zip_path, zip_name='data.zip'):
    with zipfile.ZipFile(os.path.join(zip_path, zip_name), 'w') as writer:
        for file in glob.glob(os.path.join(data_path, '*')):
            writer.write(file, os.path.basename(file))
