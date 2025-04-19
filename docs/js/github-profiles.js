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

// GitHub Profile Renderer - Simplified version
document.addEventListener('DOMContentLoaded', function() {
    // Find all elements with github-user class
    const githubUsers = document.querySelectorAll('.github-user');
    
    // Process each GitHub user reference
    githubUsers.forEach(function(element) {
        const username = element.textContent.trim().replace('@', '');
        if (!username) return;
        
        // Replace the element with a simple link to GitHub
        const link = document.createElement('a');
        link.href = `https://github.com/${username}`;
        link.target = '_blank';
        link.textContent = `@${username}`;
        link.className = 'github-link';
        
        // Replace the original element with our link
        element.parentNode.replaceChild(link, element);
    });
});