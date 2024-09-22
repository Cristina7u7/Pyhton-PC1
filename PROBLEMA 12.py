nombre_archivo=input("Ingrese el nombre del archivo: ").lower()
tipos_mime={
    ".gif":"image/gif",
    "jpg":"image/jpeg",
    ".jpeg":"image/jpeg",
    ".png":"image/png",
    ".pdf":"application/pdf",
    ".txt":"text/plain",
    ".zip":"application/zip"
}
for sufijo,mime in tipos_mime.items():
    if nombre_archivo.endswith(sufijo):
        break
else: 
    mime="application/octet-stream"
print(f"El tipo MIME es:{mime}")