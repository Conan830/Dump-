BOT_TOKEN = str(getenv('BOT_TOKEN' , '7584718311:AAHgM2r456Sz6MDCbx9uRsgRXcNPnL73se4'))
    PICS = (environ.get('PICS', 'https://envs.sh/EHp.jpg')).split()
    name = str(getenv('name', 'maheshfiletolinkbot'))
    OWNER_ID = [int(x) for x in os.environ.get("OWNER_ID", "7815873054").split()]
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'Kadali_mahesh'))

    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://hello:hello@cluster0.vc2htx0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'PaypalMafiaOfficial')) 
     
    BAN_ALERT = str(getenv('BAN_ALERT' , '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.ᴄᴏɴᴛᴀᴄᴛ @Kadali_mahesh ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>'))
    SHORTLINK = is_enabled('SHORTLINK', True)
    SHORTLINK_URL = getenv('SHORTLINK_URL', 'instantearn.in')
    SHORTLINK_API = getenv('SHORTLINK_API', '35ec2bbfc32d1b46162ce217076091ca89eea35e')
