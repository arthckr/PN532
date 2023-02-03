Import('env')
from os.path import join, realpath

# Add all files, but do not add PN532_XXX files, only add the ones that are defined
# via e.g. -DNFC_INTERFACE=HSU
for item in env.get("CPPDEFINES", []):
    if isinstance(item, tuple) and item[0] == "NFC_INTERFACE":
        env.Replace(SRC_FILTER=["+<*>", "-<PN532_*>", "+<PN532_%s.*>" % item[1]])
        break