"""
Packet Drop Simulator using POX Controller

This controller installs OpenFlow rules to drop packets
based on source IP address.

Author: Prajwal-GT
"""

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()


# 🔹 Function to install drop rule
def install_drop_rule(connection):
    """
    Installs a flow rule to drop packets from a specific source IP
    """
    msg = of.ofp_flow_mod()

    # Match only IPv4 packets
    msg.match.dl_type = 0x0800

    # Drop packets from this IP
    msg.match.nw_src = "10.0.0.1"

    # No actions = DROP
    msg.actions = []

    connection.send(msg)

    log.info("Drop rule installed for source IP 10.0.0.1")


# 🔹 Event: Switch connects
def _handle_ConnectionUp(event):
    """
    Triggered when switch connects to controller
    """
    log.info("Switch connected")

    # Install drop rule
    install_drop_rule(event.connection)


# 🔹 Main function
def launch():
    """
    Entry point for POX controller
    """
    log.info("Packet Drop Controller Started")
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
