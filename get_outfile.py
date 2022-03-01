import urllib
import sys
from mitmproxy import io, http

class Writer:
    def __init__(self, path: str) -> None:
        self.f = open(path, "wb")
        self.w = io.FlowWriter(self.f)

    def response(self, flow: http.HTTPFlow) -> None:
        self.w.add(flow)
        url = urllib.parse.unquote(flow.request.url)
        if "mp.weixin.qq.com/mp/getappmsgext" in url:
            exit()

    def done(self):

        self.f.close()

addons = [Writer(sys.argv[1])]