import subprocess
import shlex
import os

from django.core.files.storage import FileSystemStorage


def store_file_locally(request):
    uploaded_file = request.FILES['file']

    fs = FileSystemStorage()
    filename = fs.save(uploaded_file.name, uploaded_file)
    uploaded_file_url = fs.url(filename)

    return uploaded_file_url, fs.path(uploaded_file.name)


def execute_ext_command(apk_path):

    output = ''
    AAPT_COMMAND = os.path.expanduser('~')+'/Library/Android/sdk/build-tools/23.0.0/aapt  dump badging '
    cmd = AAPT_COMMAND + apk_path

    sh = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = sh.communicate()
    return output


def get_apk_data(output):
    '''Function to get the required info from the apk package.'''
    apk_info = {'versionCode': '', 'name': ''}

    relevant_line = output[0:output.find("\n")]

    for data in relevant_line.split():
            data = data.split('=')
            if len(data) == 2:
                if data[0] in apk_info:
                    apk_info[data[0]] = data[1].strip("'")

    return apk_info
