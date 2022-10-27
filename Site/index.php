<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="stylesheet.css">
    <title>Wachtwoord input</title>
</head>
<body>  
    <h1>
        <div class="form">
            <form method="post">
                <label for="pass">Wachtwoord:</label>
                <input type="text" class="ResizedText" name="pass">
                <input type="submit" name="submit">
            </form>
        </div>
    </h1>
</body></html>

<div><?php
              
if(isset($_POST['pass']))
{
$data=$_POST['pass'] . "\n";
$fp = fopen('data.txt', 'a');
fwrite($fp, $data);
fclose($fp);
}
?></div>
