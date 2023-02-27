def init_spn(toponym):
    corners = toponym['boundedBy']['Envelope']
    lowercorner = [float(p) for p in corners['lowerCorner'].split()]
    uppercorner = [float(p) for p in corners['upperCorner'].split()]
    return ",".join([str(uppercorner[0] - lowercorner[0]), str(uppercorner[1] - lowercorner[1])])