// GitHub profiles for team members
const GITHUB_PROFILES = {
  // This is a mapping of names to GitHub usernames
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

// GitHub Profile Renderer - Site-wide version
document.addEventListener('DOMContentLoaded', function() {
    // Process GitHub handles in any element
    const processGitHubHandles = function() {
        // Find all text content that might contain GitHub handles
        // This includes paragraphs, list items, table cells, headings, etc.
        const elements = document.querySelectorAll('p, li, td, th, h1, h2, h3, h4, h5, h6, span, div');
        
        elements.forEach(function(element) {
            // Skip elements that are within profile cards (to avoid reprocessing)
            if (element.closest('.github-profile-card') || 
                element.closest('.profile-card')) {
                return;
            }
            
            // Use a regex to find GitHub handles (@username format)
            // that are not within email addresses
            const text = element.innerHTML;
            if (!text) return;
            
            // Pattern: space or start of string, followed by @, followed by letters/numbers/hyphens
            // Not preceded by text that would make it an email
            const pattern = /(^|\s)@([a-zA-Z0-9-]+)(?!\S*@)/g;
            
            // Replace all instances of GitHub handles with profile cards
            element.innerHTML = text.replace(pattern, function(match, prefix, username) {
                return `${prefix}<span class="github-handle" data-username="${username}">@${username}</span>`;
            });
        });
        
        // Now process all the handles we've wrapped
        const githubHandles = document.querySelectorAll('.github-handle');
        
        githubHandles.forEach(function(handle) {
            const username = handle.getAttribute('data-username');
            if (!username) return;
            
            // Create profile card container
            const cardContainer = document.createElement('div');
            cardContainer.className = 'github-profile-card';
            
            // Add loading indicator
            cardContainer.innerHTML = `<div class="loading">Loading ${username}'s profile...</div>`;
            
            // Insert card after the handle
            handle.parentNode.insertBefore(cardContainer, handle.nextSibling);
            
            // Fetch GitHub profile data
            fetch(`https://api.github.com/users/${username}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('GitHub profile not found');
                    }
                    return response.json();
                })
                .then(data => {
                    // Create profile card with GitHub data
                    cardContainer.innerHTML = `
                        <div class="profile-card">
                            <div class="profile-image">
                                <a href="${data.html_url}" target="_blank">
                                    <img src="${data.avatar_url}" alt="${username}'s avatar">
                                </a>
                            </div>
                            <div class="profile-info">
                                <h4><a href="${data.html_url}" target="_blank">${data.name || username}</a></h4>
                                ${data.bio ? `<p class="bio">${data.bio}</p>` : ''}
                            </div>
                        </div>
                    `;
                })
                .catch(error => {
                    // If fetching fails, just show a simple link
                    cardContainer.innerHTML = `<a href="https://github.com/${username}" target="_blank">@${username}</a>`;
                    console.error('Error fetching GitHub profile:', error);
                });
        });
    };
    
    // Run processor
    processGitHubHandles();
});