import os
import sys
from shutil import copy


start_dir = ""
output_dir = ""

subject= ""
month = ""

#walk_tree traverses start_dir alterting format and output_dir
def walk_tree():
    for root, dirs, files in os.walk(start_dir):
        #Check if audio or video analysis before manipulation
        if os.path.split(root)[1] == "Audio_Analysis":
            for file in files:
                if month:
                    print "file[3:5] = {}".format(file[3:5])
                    print "file = {}".format(file)
                    if correct_audio_bl_name(file) and int(file[3:5]) == int(month):
                        copy(os.path.join(root, file), output_dir)
                else:
                    if correct_audio_bl_name(file):
                        copy(os.path.join(root, file), output_dir)
        #Check if audio or video analysis before manipulation
        if os.path.split(root)[1] == "Video_Analysis":
            for file in files:
                if month:
                    print "file[3:5] = {}".format(file[3:5])
                    print "file = {}".format(file)
                    if correct_video_bl_name(file) and int(file[3:5]) == int(month):
                        copy(os.path.join(root, file), output_dir)
                else:
                    if correct_video_bl_name(file):
                        copy(os.path.join(root, file), output_dir)


#Helper function used in walk_tree -- boolean (check for .csv; audio; ready; ".")
def correct_audio_bl_name(name):
    if name.endswith(".csv") and ("audio" in name)\
        and ("ready" not in name) and (not name.startswith(".")):
            return True
    return False

#Helper function used in walk_tree -- boolean (check for .csv; video; ready; ".")
def correct_video_bl_name(name):
    if name.endswith(".csv") and ("video" in name)\
        and ("ready" not in name) and (not name.startswith(".")):
            return True
    return False

if __name__ == "__main__":

    #Initialize and assign values to start_dir; output_dir
    start_dir = sys.argv[1]
    output_dir = sys.argv[2]

    #Initialize and assign values to "subject" and "month" 
    subject = sys.argv[3]
    month = sys.argv[4]

    if subject == "--all":
        subject = ""
    if month == "--all":
        month = ""


    walk_tree()