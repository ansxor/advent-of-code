<?php
ini_set('display_errors', '1');
ini_set('display_startup_errors', '1');
error_reporting(E_ALL);

$test_input = [
	'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
	'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
	'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
	'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
	'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
];

const MAX_RED = 12;
const MAX_GREEN = 13;
const MAX_BLUE = 14;
const INPUT_OFFSET = 5;

function part_a($input) {
	$total = 0;
	foreach ($input as &$line) {
		$game_id = intval(substr($line, INPUT_OFFSET, strpos($line, ":") - INPUT_OFFSET));
		$rounds = explode("; ", substr($line, strpos($line, ": ")+2));
		foreach ($rounds as &$round) {
			$draws = explode(", ", $round);
			foreach($draws as &$draw) {
				[$count, $colour] = explode(" ", $draw);
				$count = intval($count);
				switch ($colour) {
				case 'red':
					if ($count > MAX_RED) {
						goto fuck_this;
					}
					break;
					
				case 'green':
					if ($count > MAX_GREEN) {
						goto fuck_this;
					}
					break;
					
				case 'blue':
					if ($count > MAX_BLUE) {
						goto fuck_this;
					}
					break;
					
				default:

					break;
				}
			}
		}
		$total += $game_id;
		fuck_this:
	}
	echo($total);
}


function part_b($input) {
	$total = 0;
	foreach ($input as &$line) {
		$game_id = intval(substr($line, INPUT_OFFSET, strpos($line, ":") - INPUT_OFFSET));
		$rounds = explode("; ", substr($line, strpos($line, ": ")+2));
		$colours = [
			'red' => 0,
			'green' => 0,
			'blue' => 0
		];
		foreach ($rounds as &$round) {
			$draws = explode(", ", $round);
			foreach($draws as &$draw) {
				[$count, $colour] = explode(" ", $draw);
				$count = intval($count);
				$colours[$colour] = max($colours[$colour], $count);
			}
		}
		$total += $colours['red'] * $colours['green'] * $colours['blue'];
		fuck_this:
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
<form action="/day2/day2.php" method="POST">
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
<form action="/day2/day2.php" method="POST">
	<textarea id="input_2" name="input"></textarea>
	<input type="hidden" id="partb" name="partb" />
	<input type="submit" value="Submit" />
</form>
