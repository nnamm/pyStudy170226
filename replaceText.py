import sys
import os

TARGET_TEXT = 'a data-flickr-embed'                 # Replacement target
SRC_STRING = '"></a><script'                        # Text before replacement
DST_STRING = '" class="aligncenter></a><script'     # Text after replacement 
NEW_LINE1 = '　' + '\n' + '\n'                       # Format text1
NEW_LINE2 = '\n' + '　' + '\n'                       # Format text2

# Conform user action
if input('Overwrite the file? --> [y/n]: ') != 'y':
    print('Process ends.')
    sys.exit()

# Init process
try:
    args = sys.argv                                 # Set argument(File Name)
    file_name = args[1]                             #
    src_file = open(file_name, 'r')                 # Open source file
    tmp_file = open('TEMP_' + file_name, 'w')       # Create temp file
except IndexError:
    print('Not exist argumet.')
    sys.exit()
except IOError:
    print('Cannot open file.')
    sys.exit()

# Format the text to temp_file
rep_count = 0
for l in src_file:
    # Set 'DOUBLE_BYTE SPACE' before & after the target_text
    if TARGET_TEXT in l:
        tmp_file.write(NEW_LINE1)
        tmp_file.write(l.replace(SRC_STRING, DST_STRING))
        tmp_file.write(NEW_LINE2)
        rep_count += 1
    else:
        tmp_file.write(l)

src_file.close()                                    # Close source file
tmp_file.close()                                    # Save temp file
print('Replaced line number: ' + str(rep_count) + ' line(s)')

# Finalize process
os.remove(os.getcwd() + '/' + file_name)            # Remove source file
os.rename('TEMP_' + file_name, file_name)           # Create new source_file