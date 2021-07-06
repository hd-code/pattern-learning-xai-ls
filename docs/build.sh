# get pandoc to transform markdown files to pdf
docker pull pandoc/latex

# compile "Handbuch"
docker run --rm -v ${PWD}:/data pandoc/latex -o Handbuch.pdf Handbuch.md
