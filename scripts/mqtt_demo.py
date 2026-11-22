import argparse
from vlm.iot.events import AlertEvent
from vlm.iot.mqtt import publish_event
p=argparse.ArgumentParser()
p.add_argument("--host",default="localhost")
p.add_argument("--port",type=int,default=1883)
p.add_argument("--publish",action="store_true",help="Actually send the demo event")
a=p.parse_args()
e=AlertEvent(source_video="SYNTHETIC_DEMO",event_type="demo_alert",summary="Synthetic example; not model inference",model_id="none")
publish_event(e,host=a.host,port=a.port,dry_run=not a.publish)
