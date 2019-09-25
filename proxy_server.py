from http.server import HTTPServer, BaseHTTPRequestHandler
import browser
import optparse


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response_only(200)
        self.end_headers()

        cookie = self.headers['Cookie']
        host_url = self.headers['Host']
        browser.open(host_url, cookie, secure=not args.insecure)


def main():
    with HTTPServer(("127.0.0.1", args.port), SimpleHTTPRequestHandler) as httpd:
        httpd.serve_forever()


def parse_args():
    parser = optparse.OptionParser()
    parser.add_option('-p', '--port', help='Listen port (default 8000)',
                      default=8000, type=int)
    parser.add_option('-x', '--insecure', action='store_true', default=False,
                      help='Open webpage in insecure mode, aka HTTP (default false)')
    return parser.parse_args()[0]


if __name__ == '__main__':
    args = parse_args()
    main()
