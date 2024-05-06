
from cmdtemplate import CommandTemplate

class LedMeter(CommandTemplate):
    helpstr = "meter,<pct 0-100>"
    cfgstr = "start,stop..."

    def config(self, cfglist):
        self._start = int(cfglist[2])
        self._stop = int(cfglist[3])

    def render(self, parmlist, framebuf):
        pix = framebuf
        dot0 = self._start
        numdots = self._stop - self._start
        pct = int(parmlist[1])
        litdots = (numdots * pct) // 100
        for idx in range(litdots):
            # calculate percentage of red and green
            # for low idx it is mostly red and idx gets bigger
            # the red decreases and the green increases
            red = (64 * (numdots - idx)) // numdots
            green = (64 * idx) // numdots
            pix[dot0 + idx] = (green << 16) + (red << 8)
        for idx in range(litdots, numdots):
            pix[dot0 + idx] = 0
        return None     # no further calls needed
