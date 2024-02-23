import kopf

@kopf.on.event('pods', labels={'secret-handshake': kopf.PRESENT})
async def pod_in_sight(status, namespace, name, logger, event, **_):
    if status.get('phase') != 'Running' or event.get('type') == 'DELETED':
        return
    podIP = status.get('podIP', '')
    if not podIP:
        return
    logger.info(f"=== Found {name} in {namespace} namespace w/status: {status}")

    #logger.debug("===")