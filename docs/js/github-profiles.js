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

// GitHub Profile Renderer - Fixed version
document.addEventListener('DOMContentLoaded', function() {
    // Process table cells with GitHub handles
    const processGitHubHandles = function() {
        // Find all table cells in the document
        const tableCells = document.querySelectorAll('td, th');
        
        tableCells.forEach(function(cell) {
            const text = cell.textContent.trim();
            // Check if the cell contains ONLY a GitHub handle (starts with @ and not an email)
            if (text.startsWith('@') && text.length > 1 && !text.includes('@', 1)) {
                const username = text.substring(1); // Remove the @ symbol
                
                // Clear the cell content
                cell.innerHTML = '';
                
                // Create profile card container
                const cardContainer = document.createElement('div');
                cardContainer.className = 'github-profile-card';
                
                // Add loading indicator
                cardContainer.innerHTML = `<div class="loading">Loading ${username}'s profile...</div>`;
                
                // Add the card to the cell
                cell.appendChild(cardContainer);
                
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
            }
        });
    };
    
    // Process all table cells
    processGitHubHandles();
});