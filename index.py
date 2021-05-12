import os

def generate_index(path,file):
    filepath = os.path.join(path,"index.html")
    with open(filepath, "w") as f:
        f.write("<html><body><ul>\n")
        f.write(f"<img src = '{file}'>\n")
        f.write("</ul></body></html>\n")
