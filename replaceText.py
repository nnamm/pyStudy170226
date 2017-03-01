import sys

TARGET_TEXT = 'a data-flickr-embed'                 # Replacement target
SRC_STRING = '"></a><script'                        # Text before replacement
DST_STRING = '" class="aligncenter></a><script'     # Text after replacement 
NEW_LINE = '\n' + '　' + '\n'                        # Formatting text

# Init process
try:
    args = sys.argv                                 # Set argument(File Name)
    file_name = args[1]                             #
    src_file = open(file_name, 'r')                 # Open file
    new_file = open('NEW_' + file_name, 'w')        # Create new file
except IndexError:
    print('Not exist argumet')
    sys.exit()
except IOError:
    print('Cannot open file.')
    sys.exit()
except:
    print('System error.')
    sys.exit()

# Format the text
for l in src_file:
    # Set 'DOUBLE_BYTE SPACE' before & after the target_text.
    if TARGET_TEXT in l:
        new_file.write(NEW_LINE)
        new_file.write(l.replace(SRC_STRING, DST_STRING))
        new_file.write(NEW_LINE)
    else:
        new_file.write(l)

src_file.close()                                    # Close the src file.
new_file.close()                                    # Save the new file.
