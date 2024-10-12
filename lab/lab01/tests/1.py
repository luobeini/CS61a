import urllib.parse

encoded_str = "#list/path=%2F?cuid=baidutiebaappef6c6cc3-33e7-47f3-93eb-907f[#list/path=%2F?cuid=baidutiebaappef6c6cc3-33e7-47f3-93eb-907fdf36048 1&cuid_galaxy2=6995AA576AA9FOEDCEO3340086D18C20 V3T3E7NFN&cuid_gid=Xtamp=1610110063569&_ client_version=12.2.8.1&nohead=1]"
decoded_str = urllib.parse.unquote(encoded_str)
print(decoded_str)