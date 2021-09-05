FROM python:3.8
COPY sort_codenames_words_in_file.py .
CMD ["python", "sort_codenames_words_in_file.py"]


# Build Using Docker
# 1. Build the image:
#    docker build -t sort-words .
# 2. Create the container and run:
#    docker run -d -v <path_to_codenames-words_repo>\dictionaries:/dictionaries --name sort-words-1 sort-words
