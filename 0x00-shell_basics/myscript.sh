#!/bin/bash

echo "Enter filename: "
read filename
echo "Enter command: "
read command

touch ./${filename}
echo '#!/bin/bash' > ${filename}
echo $command >> ${filename}

chmod u+x ${filename}

git add .
git commit -m "Added $filename"
git push


