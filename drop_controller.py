from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_PacketIn(event):
    packet = event.parsed

    # Example: Drop traffic from h1 (port 1)
    if event.port == 1:
        log.info("Dropping packet from port 1")
        return  # DROP (no action)

    # Otherwise forward normally
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Packet Drop Controller Running")
