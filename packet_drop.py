from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_ConnectionUp(event):
    log.info("Switch connected")

    # DROP RULE
    msg = of.ofp_flow_mod()
    msg.match.dl_type = 0x0800
    msg.match.nw_src = "10.0.0.1"
    msg.actions = []

    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
