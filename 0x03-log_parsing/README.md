<h2>Write a script that reads stdin line by line and computes metrics:</h2>

<strong>Input format:</strong><br/>
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size><br/>
(if the format is not this one, the line must be skipped)<br/><br/>
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
- <strong>Total file size:</strong> File size: <total size><br/>
- where <total size> is the sum of all previous <file size> (see input format above)<br/>
- Number of lines by status code:
  *possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
  *if a status code doesn’t appear or is not an integer, don’t print anything for this status code
  *format: <status code>: <number>
  *status codes should be printed in ascending order
