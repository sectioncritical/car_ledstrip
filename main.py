
import array
import cmdif
import ws2812_pio as wspio

ws = wspio.WS2812(0, 16)
pixels = array.array("I", [0 for _ in range(144)])

def meter(param_list, config_list):
    global pixels
    dot0 = config_list[0]
    numdots = config_list[1]
    pct = int(param_list[1])
    litdots = (numdots * pct) // 100
    for idx in range(litdots):
        red = (64 * (numdots - idx)) // numdots
        green = (64 * idx) // numdots
        pixels[dot0 + idx] = (green << 16) + (red << 8)
    for idx in range(litdots, numdots):
        pixels[dot0 + idx] = 0
    ws.show(pixels)

meter_config = [0, 40]

ci = cmdif.CmdInterface()
ci.add_cmd("meter", meter, "bar meter red to green (0-100)", meter_config)

ci.run()
