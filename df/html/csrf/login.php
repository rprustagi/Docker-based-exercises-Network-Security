<?php
session_start();

$users = json_decode(file_get_contents(__DIR__ . '/users.json'), true);

$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $user = $_POST['username'] ?? '';
    $pass = $_POST['password'] ?? '';

    if (isset($users[$user]) && $users[$user] === $pass) {
        $_SESSION['user'] = $user;
        setcookie("auth", "authenticated", time() + 3600, "/");
        header("Location: bank.php");
        exit;
    } else {
        $error = "Invalid username or password.";
    }
}
?>

<!DOCTYPE html>
<html>
<head><title>Bank Login</title></head>
<body>
  <h2>Login to Your Bank Account</h2>
  <?php if ($error): ?>
    <p style="color:red"><?= htmlspecialchars($error) ?></p>
  <?php endif; ?>
  <form method="post">
    Username: <input type="text" name="username" required><br>
    Password: <input type="password" name="password" required><br>
    <button type="submit">Login</button>
  </form>
</body>
</html>
