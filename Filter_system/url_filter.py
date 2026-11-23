
Image_Extensions = [
    ".jpg", ".jpeg", ".png", ".gif",
    ".webp", ".svg", ".avif"
     ] 

Video_Extensions = [
    ".mp4", ".mov", ".avi", ".mkv",
    ".webm", ".m3u8"
     ]

Document_Extensions = [
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"
     ]

Audio_Extensions = [
    ".mp3", ".wav", ".flac", ".aac",
     ]

Non_Article_Keywords = [
    "/category/",
    "/tag/",
    "/author/",
    "/search/",
    "/login/",
    "/signup/",
    "/contact/",
    "/about/",
    "/gallery/",
    "/video/",
    "/videos/"
]


def filter_url(url):

    for keyword in Image_Extensions:
        if keyword in url:
            return False

     
    for keyword in Video_Extensions:
        if keyword in url:
            return False


    for keyword in Document_Extensions:
        if keyword in url:
            return False

    for keyword in Audio_Extensions:
        if keyword in url:
            return False


    for keyword in  Non_Article_Keywords:
        if keyword in url:
            return False

    return True

    