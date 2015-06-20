class player_info ( object ):
    def __init__ ( self,
                   deaths = None,
                   health = None,
                   home = None,
                   ip = None,
                   level = None,
                   name = None,
                   online = None,
                   playerid = None,
                   players = None,
                   pos_x = None,
                   pos_y = None,
                   pos_z = None,
                   score = None,
                   steamid = None,
                   zombies = None ):
        super ( player_info, self ).__init__ ( )

        # Attributes received from lp:
        self.deaths = deaths
        self.health = health
        self.home = home
        self.ip = ip
        self.level = level
        self.name = name
        self.online = online
        self.playerid = playerid
        self.players = players
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.score = score
        self.steamid = steamid
        self.zombies = zombies

        # Attributes received from mods:
        self.home_invasion_beacon = None
        self.home_invitees = [ ]
        self.language_preferred = None
        self.languages_spoken = [ ]
        self.map_limit_beacon = None
        self.name_sane = None

        # Extensible attributes dictionary:
        self.attributes = { }