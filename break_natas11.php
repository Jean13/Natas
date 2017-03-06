<?php

$p_text = json_encode(array("showpassword"=>"no", "bgcolor"=>"#ffffff"));
$c_text = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=");

function xor_encrypt($in, $k) {
    $key = $k;
    $text = $in;
    $outText = '';

    for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

//print xor_encrypt($p_text, $c_text);

// The key was added after running the code above by itself.
$the_key = "qw8J";
$plaintext = array("showpassword"=>"yes", "bgcolor"=>"#ff0000");

print base64_encode(xor_encrypt(json_encode($plaintext), $the_key));

?>
