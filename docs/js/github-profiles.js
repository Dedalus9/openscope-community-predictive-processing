// GitHub profiles for team members
const GITHUB_PROFILES = {
  // This is a mapping of names to GitHub usernames
  // Add actual usernames as you collect them from team members
  "Jérôme A. Lecoq": "jeromelecoq",
  "André M. Bastos": "andremarcosbastos",
  "Farzaneh Najafi": "fnajafi",
  "Sarah Ruediger": "sruediger",
  // Add more team members and their GitHub usernames here
  // Format: "Full Name": "github-username",
};

// Function to get GitHub username by person's name
function getGitHubUsername(fullName) {
  return GITHUB_PROFILES[fullName] || null;
}

// Export the functions and data for use in other scripts
if (typeof module !== 'undefined') {
  module.exports = {
    GITHUB_PROFILES,
    getGitHubUsername
  };
}

// GitHub Profile Renderer - Enhanced version
document.addEventListener('DOMContentLoaded', function() {
    // Process table cells with GitHub handles
    const processGitHubHandles = function() {
        // Find all table cells in the document
        const tableCells = document.querySelectorAll('td, th');
        
        tableCells.forEach(function(cell) {
            const text = cell.textContent.trim();
            // Check if the cell contains a GitHub handle (starts with @)
            if (text.startsWith('@') && text.length > 1) {
                const username = text.substring(1); // Remove the @ symbol
                
                // Clear the cell and create a link
                cell.innerHTML = '';
                
                const link = document.createElement('a');
                link.href = `https://github.com/${username}`;
                link.target = '_blank';
                link.textContent = `@${username}`;
                link.className = 'github-link';
                
                cell.appendChild(link);
            }
        });
    };
    
    // First approach: Process explicit github-user spans
    const githubUsers = document.querySelectorAll('.github-user');
    
    githubUsers.forEach(function(element) {
        const username = element.textContent.trim().replace('@', '');
        if (!username) return;
        
        // Replace with a GitHub link
        const link = document.createElement('a');
        link.href = `https://github.com/${username}`;
        link.target = '_blank';
        link.textContent = `@${username}`;
        link.className = 'github-link';
        
        element.parentNode.replaceChild(link, element);
    });
    
    // Second approach: Auto-detect GitHub usernames in text
    // Look for GitHub username patterns in the document - @username format
    const detectGitHubUsernames = function(node) {
        if (node.nodeType === 3) { // Text node
            const text = node.nodeValue;
            // Match GitHub username pattern: @username
            // Username requirements: 
            // - starts with @
            // - followed by letters, numbers, or hyphens (no spaces)
            // - at least 1 character long
            const regex = /@([a-zA-Z0-9-]+)/g;
            let match;
            let lastIndex = 0;
            const fragments = [];
            
            while ((match = regex.exec(text)) !== null) {
                // Text before the match
                if (match.index > lastIndex) {
                    fragments.push(document.createTextNode(text.substring(lastIndex, match.index)));
                }
                
                // The username
                const username = match[1];
                const link = document.createElement('a');
                link.href = `https://github.com/${username}`;
                link.target = '_blank';
                link.textContent = `@${username}`;
                link.className = 'github-link auto-detected';
                fragments.push(link);
                
                lastIndex = regex.lastIndex;
            }
            
            // Text after the last match
            if (lastIndex < text.length) {
                fragments.push(document.createTextNode(text.substring(lastIndex)));
            }
            
            // Replace the text node with the fragments
            if (fragments.length > 1) {
                const parent = node.parentNode;
                fragments.forEach(function(fragment) {
                    parent.insertBefore(fragment, node);
                });
                parent.removeChild(node);
                return true;
            }
        }
        return false;
    };
    
    // Process all text nodes in the document body
    const walk = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
    const nodes = [];
    let node;
    while ((node = walk.nextNode())) {
        nodes.push(node);
    }
    
    // Process nodes in reverse order to maintain correct indices
    for (let i = nodes.length - 1; i >= 0; i--) {
        detectGitHubUsernames(nodes[i]);
    }
    
    // Also process table cells specifically (which may not be caught by the text walker)
    processGitHubHandles();
});