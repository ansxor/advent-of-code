<?php
ini_set('display_errors', '1');
ini_set('display_startup_errors', '1');
error_reporting(E_ALL);

$test_input = [
	'1abc2',
	'pqr3stu8vwx',
	'a1b2c3d4e5f',
	'treb7uchet'
];

$test_input_2 = [
	'two1nine',
	'eightwothree',
	'abcone2threexyz',
	'xtwone3four',
	'4nineeightseven2',
	'zoneight234',
	'7pqrstsixteen'
];

function part_a($input) {
	$total = 0;
	foreach ($input as &$line) {
		$transformed_line = array_filter(str_split($line), 'is_numeric');
		$total += intval(reset($transformed_line) . end($transformed_line));
	}
	echo($total);
}


function part_b($input) {
	$map_words = [
		'one' => '1',
		'two' => '2',
		'three' => '3',
		'four' => '4',
		'five' => '5',
		'six' => '6',
		'seven' => '7',
		'eight' => '8',
		'nine' => '9',
	];
	$total = 0;
	foreach ($input as $line) {
		$first = NULL;
		$last = NULL;
		$i = 0;
		while ($i < strlen($line)) {
			foreach ($map_words as $word => $number) {
				if (strcmp(substr($line, $i, strlen($word)), $word) === 0) {
					if ($first === NULL) {
						$first = $number;
					}
					$last = $number;
					break;
				}
			}

			$single = substr($line, $i, 1);
			if (is_numeric($single)) {
				$val = intval($single);
				if ($first === NULL) {
					$first = $val;
				}
				$last = $val;
			}
			$i += 1;
		}
		$total += intval($first . $last);
	}
	echo($total);
}

?>

<h1>
part 1
</h1>
<p>
<?php
if (array_key_exists('parta', $_POST)) {
	$input = preg_split('/\r\n|[\r\n]/', $_POST['input']);
	part_a($input);
}
?>
</p>
<form action="/day1/day1.php" method="POST">
	<textarea id="input" name="input"></textarea>
	<input type="hidden" id="parta" name="parta" />
	<input type="submit" value="Submit" />
</form>

<h1>
part 2
</h1>
<p>
<?php
if (array_key_exists('partb', $_POST)) {
	$input = preg_split('/\r\n|[\r\n]/', $_POST['input']);
	part_b($input);
}
?>
</p>
<form action="/day1/day1.php" method="POST">
	<textarea id="input_2" name="input"></textarea>
	<input type="hidden" id="partb" name="partb" />
	<input type="submit" value="Submit" />
</form>
