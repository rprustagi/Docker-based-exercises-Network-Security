<?php
session_start();

// Require login
if (!isset($_SESSION['user']) || ($_COOKIE['auth'] ?? '') !== 'authenticated') {
    header("Location: login.php");
    exit;
}

$user = $_SESSION['user'];
$log_file = __DIR__ . '/transactions.txt';
$status = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $to = $_POST['to'] ?? 'unknown';
    $amount = $_POST['amount'] ?? '0';
    $timestamp = date('Y-m-d H:i:s');
    $log_entry = "[$timestamp] $user sent $amount to $to\n";

    if (file_put_contents($log_file, $log_entry, FILE_APPEND) !== false) {
        $status = "<p style='color:green'> Transaction recorded:</p><pre>$log_entry</pre>";
    } else {
        $status = "<p style='color:red'> Failed to write transaction.</p>";
    }
}
?>

<!DOCTYPE html>
<html>
<head><title>Welcome to Your Bank</title></head>
<body>
  <h1>Hello, <?= htmlspecialchars($user) ?>!</h1>
  <p><a href="logout.php">Logout</a></p>

  <h3>Transfer Money</h3>
  <form method="post">
    Send Money To: <input name="to" ><br>
    Amount: <input name="amount" ><br>
    <button type="submit">Transfer</button>
  </form>

  <?= $status ?>
</body>
</html>
