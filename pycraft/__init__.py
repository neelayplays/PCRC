"""
A modern, Python3-compatible, well-documented library for communicating
with a MineCraft server.
"""

# The version number of the most recent pyCraft release.
__version__ = "0.6.0"

# A dict mapping the ID string of each Minecraft version supported by pyCraft
# to the corresponding protocol version number. The ID string of a version is
# the key used to identify it in
# <https://launchermeta.mojang.com/mc/game/version_manifest.json>, or the 'id'
# key in "version.json" in the corresponding ".jar" file distributed by Mojang.
SUPPORTED_MINECRAFT_VERSIONS = {
    '1.8':                  47,
    '1.8.1':                47,
    '1.8.2':                47,
    '1.8.3':                47,
    '1.8.4':                47,
    '1.8.5':                47,
    '1.8.6':                47,
    '1.8.7':                47,
    '1.8.8':                47,
    '1.8.9':                47,
    '1.9':                  107,
    '1.9.1':                108,
    '1.9.2':                109,
    '1.9.3':                110,
    '1.9.4':                110,
    '1.10':                 210,
    '1.10.1':               210,
    '1.10.2':               210,
    '16w32a':               301,
    '16w32b':               302,
    '16w33a':               303,
    '16w35a':               304,
    '16w36a':               305,
    '16w38a':               306,
    '16w39a':               307,
    '16w39b':               308,
    '16w39c':               309,
    '16w40a':               310,
    '16w41a':               311,
    '16w42a':               312,
    '16w43a':               313,
    '16w44a':               313,
    '1.11-pre1':            314,
    '1.11':                 315,
    '16w50a':               316,
    '1.11.1':               316,
    '1.11.2':               316,
    '17w06a':               317,
    '17w13a':               318,
    '17w13b':               319,
    '17w14a':               320,
    '17w15a':               321,
    '17w16a':               322,
    '17w16b':               323,
    '17w17a':               324,
    '17w17b':               325,
    '17w18a':               326,
    '17w18b':               327,
    '1.12-pre1':            328,
    '1.12-pre2':            329,
    '1.12-pre3':            330,
    '1.12-pre4':            331,
    '1.12-pre5':            332,
    '1.12-pre6':            333,
    '1.12-pre7':            334,
    '1.12':                 335,
    '17w31a':               336,
    '1.12.1-pre1':          337,
    '1.12.1':               338,
    '1.12.2-pre1':          339,
    '1.12.2-pre2':          339,
    '1.12.2':               340,
    '17w43a':               341,
    '17w43b':               342,
    '17w45a':               343,
    '17w45b':               344,
    '17w46a':               345,
    '17w47a':               346,
    '17w47b':               347,
    '17w48a':               348,
    '17w49a':               349,
    '17w49b':               350,
    '17w50a':               351,
    '18w01a':               352,
    '18w02a':               353,
    '18w03a':               354,
    '18w03b':               355,
    '18w05a':               356,
    '18w06a':               357,
    '18w07a':               358,
    '18w07b':               359,
    '18w07c':               360,
    '18w08a':               361,
    '18w08b':               362,
    '18w09a':               363,
    '18w10a':               364,
    '18w10b':               365,
    '18w10c':               366,
    '18w10d':               367,
    '18w11a':               368,
    '18w14a':               369,
    '18w14b':               370,
    '18w15a':               371,
    '18w16a':               372,
    '18w19a':               373,
    '18w19b':               374,
    '18w20a':               375,
    '18w20b':               376,
    '18w20c':               377,
    '18w21a':               378,
    '18w21b':               379,
    '18w22a':               380,
    '18w22b':               381,
    '18w22c':               382,
    '1.13-pre1':            383,
    '1.13-pre2':            384,
    '1.13-pre3':            385,
    '1.13-pre4':            386,
    '1.13-pre5':            387,
    '1.13-pre6':            388,
    '1.13-pre7':            389,
    '1.13-pre8':            390,
    '1.13-pre9':            391,
    '1.13-pre10':           392,
    '1.13':                 393,
    '18w30a':               394,
    '18w30b':               395,
    '18w31a':               396,
    '18w32a':               397,
    '18w33a':               398,
    '1.13.1-pre1':          399,
    '1.13.1-pre2':          400,
    '1.13.1':               401,
    '1.13.2-pre1':          402,
    '1.13.2-pre2':          403,
    '1.13.2':               404,
    '18w43a':               441,
    '18w43b':               441,
    '18w43c':               442,
    '18w44a':               443,
    '18w45a':               444,
    '18w46a':               445,
    '18w47a':               446,
    '18w47b':               447,
    '18w48a':               448,
    '18w48b':               449,
    '18w49a':               450,
    '18w50a':               451,
    '19w02a':               452,
    '19w03a':               453,
    '19w03b':               454,
    '19w03c':               455,
    '19w04a':               456,
    '19w04b':               457,
    '19w05a':               458,
    '19w06a':               459,
    '19w07a':               460,
    '19w08a':               461,
    '19w08b':               462,
    '19w09a':               463,
    '19w11a':               464,
    '19w11b':               465,
    '19w12a':               466,
    '19w12b':               467,
    '19w13a':               468,
    '19w13b':               469,
    '19w14a':               470,
    '19w14b':               471,
    '1.14 Pre-Release 1':   472,
    '1.14 Pre-Release 2':   473,
    '1.14 Pre-Release 3':   474,
    '1.14 Pre-Release 4':   475,
    '1.14 Pre-Release 5':   476,
    '1.14':                 477,
    '1.14.1 Pre-Release 1': 478,
    '1.14.1 Pre-Release 2': 479,
    '1.14.1':               480,
    '1.14.2 Pre-Release 1': 481,
    '1.14.2 Pre-Release 2': 482,
    '1.14.2 Pre-Release 3': 483,
    '1.14.2 Pre-Release 4': 484,
    '1.14.2':               485,
    '1.14.3-pre1':          486,
    '1.14.3-pre2':          487,
    '1.14.3-pre3':          488,
    '1.14.3-pre4':          489,
    '1.14.3':               490,
    '1.14.4-pre1':          491,
    '1.14.4-pre2':          492,
    '1.14.4-pre3':          493,
    '1.14.4-pre4':          494,
    '1.14.4-pre5':          495,
    '1.14.4-pre6':          496,
    '1.14.4-pre7':          497,
    '1.14.4':               498,
# comment for 1.14.4 recording only
#    '1.15':                 573,
#    '1.15.1':               575,
}

# Those Minecraft versions supported by pyCraft which are "release" versions,
# i.e. not development snapshots or pre-release versions.
RELEASE_MINECRAFT_VERSIONS = {
    vid: protocol for (vid, protocol) in SUPPORTED_MINECRAFT_VERSIONS.items()
    if __import__('re').match(r'\d+(\.\d+)+$', vid)}

# The protocol versions of SUPPORTED_MINECRAFT_VERSIONS, without duplicates,
# in ascending numerical (and hence chronological) order.
SUPPORTED_PROTOCOL_VERSIONS = \
    sorted(set(SUPPORTED_MINECRAFT_VERSIONS.values()))

# The protocol versions of RELEASE_MINECRAFT_VERSIONS, without duplicates,
# in ascending numerical (and hence chronological) order.
RELEASE_PROTOCOL_VERSIONS = \
    sorted(set(RELEASE_MINECRAFT_VERSIONS.values()))
