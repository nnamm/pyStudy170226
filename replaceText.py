import sys

SRC_STRING = '"></a><script'
DST_STRING = '" class="aligncenter></a><script'

# Init process
try:
    args = sys.argv                                 # Set argument(File Name)
    file_name = args[1]                             #
    src_file = open(file_name, 'r')                 # Open file
    new_file = open('NEW_' + file_name, 'w')        # Create new file
except IndexError:
    print('Usage: %s TEXTFILE')
except IOError:
    print('"%s" cannot be opened.')

# Repeat the following processing
target_text = 'a data-flickr-embed'
for l in src_file:
    if target_text in l:
        new_file.write(l.replace(SRC_STRING, DST_STRING))
    else:
        new_file.write(l)

src_file.close()
new_file.close()
