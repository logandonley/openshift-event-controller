def handle_event(watcher, event, config):
    message = "This is a test"
    log_level = config.get('message_log_level','INFO')
    return message, log_level
