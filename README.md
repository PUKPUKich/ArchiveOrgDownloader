# ArchiveOrgDownloader
With this script you can download any (probably) book from archive.org

For the script to work properly you need to “borrow” the book on your page first.
![image](https://github.com/user-attachments/assets/adaf3894-4e70-452a-86ca-962384e4ed77)

Then you need to open developer tools (ctrl + shift + i) on the site with the book, go to “Network”, open any downloaded photo and copy the link
![image](https://github.com/user-attachments/assets/ae05c7b7-08fa-4c8e-946b-8972cfe33b64)

IMPORTANT:
Before .jp2 or other extension where there are numbers 0001-1000 you need to replace them with {page_num}.jp2

Example:
Original link: https://ia601409.us.archive.org/BookReader/BookReaderImages.php?zip=/2/items/collinscobuilden0000unse_w0v8/collinscobuilden0000unse_w0v8_jp2.zip&file=collinscobuilden0000unse_w0v8_jp2/collinscobuilden0000unse_w0v8_0604.jp2&id=collinscobuilden0000unse_w0v8&scale=4&rotate=0

Correct link: https://ia601409.us.archive.org/BookReader/BookReaderImages.php?zip=/2/items/collinscobuilden0000unse_w0v8/collinscobuilden0000unse_w0v8_jp2.zip&file=collinscobuilden0000unse_w0v8_jp2/collinscobuilden0000unse_w0v8_{page_num}.jp2&id=collinscobuilden0000unse_w0v8&scale=4&rotate=0


In headers you need to specify your cookie and referer link just by copying them from Request Headers

Then just run the .py file
