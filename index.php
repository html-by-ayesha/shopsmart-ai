<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);
    
    $age      = escapeshellarg($data['age']);
    $budget   = escapeshellarg($data['budget']);
    $gender   = escapeshellarg($data['gender']);
    $interest = escapeshellarg($data['interest']);
    
    $script_path = __DIR__ . '\\predict.py';
    
    // Try multiple python paths
    $python_paths = ['python', 'python3', 'py'];
    $output = null;
    
    foreach ($python_paths as $python) {
        $command = "$python \"$script_path\" $age $budget $gender $interest 2>&1";
        $output = shell_exec($command);
        if ($output && strpos($output, 'recommended') !== false) {
            break;
        }
    }
    
    // Extract JSON from output
    if ($output) {
        $lines = explode("\n", trim($output));
        $json_line = '';
        foreach ($lines as $line) {
            if (strpos($line, '{') !== false) {
                $json_line = $line;
            }
        }
        
        $result = json_decode($json_line, true);
        
        if ($result) {
            echo json_encode($result);
        } else {
            echo json_encode([
                "error" => "Parse error",
                "raw" => $output
            ]);
        }
    } else {
        echo json_encode(["error" => "Python not found"]);
    }
} else {
    echo json_encode(["error" => "Invalid request"]);
}
?>