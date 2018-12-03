from datetime import datetime, timedelta


def relative_time_format(time: datetime) -> str:

    now = datetime.utcnow()
    if time < now.replace(year=now.year-1):
        return time.strftime("%Y-%m-%d %H:%M:%S")
    elif time < now - timedelta(days=7):
        return time.strftime("%b %d %H:%M:%S")
    elif time < now - timedelta(days=1):
        return time.strftime("%a %H:%M:%S")
    elif time < now - timedelta(hours=6):
        return time.strftime("%H:%M:%S")
    elif time < now - timedelta(minutes=90):
        return 'about {} hours ago'.format(round((now - time).total_seconds()/3600))
    elif time < now - timedelta(minutes=60):
        return 'about an hour ago'
    elif time < now - timedelta(minutes=2):
        return '{} minutes ago'.format(round((now - time).total_seconds()/60))
    else:
        return 'a moment ago'
