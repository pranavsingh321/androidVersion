import axmlparserpy.apk as apk


def get_apk_data(apk_path):
	'''Function to get the required info from the apk package.'''
	apk_info = {}

	apk_obj = apk.APK(apk_path)
	apk_info['package_name'] = apk_obj.get_package()
	apk_info['package_version'] = apk_obj.get_androidversion_name()

	return apk_info

def save_apk_file(apk_path):
	pass
    	