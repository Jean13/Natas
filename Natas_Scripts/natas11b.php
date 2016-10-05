<?php

$p_text = array("showpassword"=>"yes", "bgcolor"=>"#ff0000");
$key = "qw8J";

function xor_encrypt($in, $k) {
    $key = $k;
    $text = $in;
    $outText = '';

    for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

print base64_encode(xor_encrypt(json_encode($p_text), $key));

?>
